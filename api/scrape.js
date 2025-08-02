import * as cheerio from 'cheerio'; // ✅ CORRECT

import axios from 'axios';

export default async function handler(req, res) {
  const { q = '' } = req.query;

  if (!q) return res.status(400).json({ error: 'Missing query' });

  const url = `https://www.alevelapi.com/?s=${encodeURIComponent(q)}`;

  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);
    const results = [];

    $('ul.post-items li.post-item').each((_, el) => {
      const title = $(el).find('h2.entry-title a').text().trim();
      const link = $(el).find('h2.entry-title a').attr('href');
      const thumbnail = $(el).find('.post-thumbnail img').attr('src') || null;

      results.push({ title, link, thumbnail });
    });

    return res.status(200).json({ query: q, results });
  } catch (error) {
    return res.status(500).json({ error: 'Scrape failed', detail: error.message });
  }
}
