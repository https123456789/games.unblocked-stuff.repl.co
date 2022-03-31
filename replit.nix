{ pkgs }: {
	deps = [
		pkgs.nodejs-16_x
        pkgs.nodePackages.typescript-language-server
        pkgs.nodePackages.yarn
        pkgs.replitPackages.jest
		pkgs.python39Full
		pkgs.python39Packages.pip
		pkgs.python39Packages.poetry
		pkgs.python39Packages.requests
	];
}