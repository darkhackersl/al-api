{ pkgs }: {
  deps = [
    pkgs.python310Full
    pkgs.python310Packages.flask
    pkgs.python310Packages.playwright
    pkgs.glib
    pkgs.glibc
    pkgs.libx11
    pkgs.libxcomposite
    pkgs.libxdamage
    pkgs.libxrandr
    pkgs.libxss
    pkgs.libxtst
    pkgs.gtk3
    pkgs.nss
    pkgs.libsecret
    pkgs.libatk
    pkgs.cups
    pkgs.libdrm
    pkgs.gcc
    pkgs.fontconfig
    pkgs.freetype
    pkgs.libpng
    pkgs.libtiff
  ];
}
