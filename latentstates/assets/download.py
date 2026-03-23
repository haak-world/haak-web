#!/usr/bin/env python3
"""Download Latent States visual assets from Google Drive via gcloud auth."""

import subprocess
import sys
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError

OUT_DIR = Path(__file__).parent

ASSETS = {
    # Film stills - Latent Space (AI-generated dream imagery)
    "1-1WYep_hG8oowCD56lCTMDwP8OYuztbF": "ls-dark-eyes-1.jpg",
    "1sNP88I62oWHQEXobvDAJVzGQxoM-OqYE": "ls-dark-eyes-2.jpg",
    "1xawSS8v6vn6nu74tzkzTaqtll7U5fjbw": "ls-whale-ai.jpg",
    "1ZyHvWmmWpyOh1ZCAOPB_hfRALGIaMyWy": "ls-ocean.jpg",
    "1SBjNyeNrCKPRTak76tqKTNf5beVUKqns": "ls-mirror.jpg",
    "1jOkBZM_HPH88XyESXuopWrb45cMMDjre": "ls-sintra.jpg",
    "12433YB5QfU7wCjOdyxlGjEQFI02x4QW3": "ls-sintra-2.jpg",
    "1EzmoevTGTsuuK0JLojMaAOrYnap660Aw": "ls-the-cube.jpg",
    "1wcpXojuH6xg6BighXWU0qszPUZlDOqhD": "ls-beautiful-woman.jpg",
    "1s_3E8r-Nbyh_OyWnHoYxtroAD-jG1O3F": "ls-aged-siori-lee.jpg",
    "1F8MaBIq-MJcKD0M8_pBUk-_D0_pGTA_h": "ls-sand-castle-ai.jpg",
    "1zu_K-GnoX_PahQSlKBlPGNRHNoFwFxm3": "ls-banana-hands-ai.jpg",
    # Metamersion banners/posters
    "1R1CHV0e77NcAzllWFZfuohSzjumJre_m": "metamersion-banner-v4.png",
    "1G5c7VexPz7LSHSaYa1HIuBPPOiVawKtX": "metamersion-poster1.png",
    "1R1PsCrlXgTNkz16WLWhMPL7khbkd6zkA": "metamersion-banner.png",
    # Metamersion poster PDF
    "1EU6wSY1k0brzNsHms2of1aKuhtaaGnYh": "metamersion-poster-af.pdf",
    # Boom festival
    "1vfgyUUcj5gbSOe33Ikm_XozCEdRnDJ8c": "boom-remember-who-you-are-2014.jpg",
    # Latent State 2025 photos (warehouse/installation)
    "17uMZAmGRlBfL26tjFOuHmUOddRLv4-qy": "ls-2025-warehouse-01.jpg",
    "17uiw-if8d94kCgk0LT15LOddEz1y3ijq": "ls-2025-warehouse-02.jpg",
    "17wnm5uFRCvG_gnkYmRqWpP6ubbELPnGd": "ls-2025-warehouse-03.jpg",
    "180pzK5lIssFijKVwhgAEFsyGrbDJtNip": "ls-2025-warehouse-04.jpg",
    "185vDSNyYqa4gHaCtN0NUyBdNnde6Uxz-": "ls-2025-warehouse-05.jpg",
}


def get_token():
    result = subprocess.run(
        ["gcloud", "auth", "print-access-token"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print("Failed to get gcloud token:", result.stderr)
        sys.exit(1)
    return result.stdout.strip()


def download_file(token, file_id, filename):
    url = f"https://www.googleapis.com/drive/v3/files/{file_id}?alt=media"
    req = Request(url, headers={"Authorization": f"Bearer {token}"})
    try:
        resp = urlopen(req)
        out = OUT_DIR / filename
        with open(out, "wb") as f:
            while True:
                chunk = resp.read(8192)
                if not chunk:
                    break
                f.write(chunk)
        size_kb = out.stat().st_size / 1024
        print(f"  OK  {filename} ({size_kb:.0f} KB)")
        return True
    except HTTPError as e:
        print(f"  FAIL {filename} — HTTP {e.code}: {e.reason}")
        return False


def main():
    token = get_token()
    ok, fail = 0, 0
    for fid, fname in ASSETS.items():
        if download_file(token, fid, fname):
            ok += 1
        else:
            fail += 1
    print(f"\nDone: {ok} downloaded, {fail} failed")


if __name__ == "__main__":
    main()
