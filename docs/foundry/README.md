# Public package presentation

This directory contains the versioned presentation assets for the Foundry VTT package page.

- `description-foundry.html` is the HTML fragment to paste into the package description on
  foundryvtt.com. It is deliberately not used as `module.json`'s short `description`.
- `assets/banner-srd-2024.webp` and `assets/screenshots/` are referenced through their raw GitHub
  URLs. Publish them on the default branch before pasting the HTML into Foundry.

## Publication check

1. Commit the banner, the four screenshots, and `description-foundry.html`.
2. Verify that each `raw.githubusercontent.com` URL in the HTML serves its intended image.
3. Paste the HTML fragment in the public package editor and review the resulting desktop and mobile
   views.
4. Keep compatibility claims aligned with `module.json`; updating this page does not require a
   module release.

The source prototype is retained at the workspace level in
`docs/foundry-srd-presentation/`. It is reference material; the files in this directory are the
module-owned publication artifacts.
