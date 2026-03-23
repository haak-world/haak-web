#!/usr/bin/env python3
"""Download key visual assets from Google Drive for latentstates.org."""

import json, os, sys, requests

CREDS_PATH = os.path.expanduser("~/.config/google-drive-mcp/gcp-oauth.keys.json")
TOKENS_PATH = os.path.expanduser("~/.config/google-drive-mcp/tokens.json")
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# Target files: (file_id, output_filename)
# Note: files on zmainen@neuro.fchampalimaud.org are NOT accessible from the
# zmainen@fchampalimaud.org OAuth token. Only shared files and files owned by
# that account or shared to it will download.
TARGETS = [
    # Metamersion A2 posters (high-res, ~11MB each) — great hero images
    ("1dDihDEmZ2ak3b82dtXXn4wiGN59Y9NH1", "metamersion-poster-a2-v1.png"),
    ("11uS5bHFjG6nUWsPoI_RvLi4H9dDI4eP9", "metamersion-poster-a2-v2.png"),
    ("1whnw3sxwaziEbCzcsOJnlGGseID3J16C", "metamersion-poster-a2-v3.png"),
    # Metamersion Eventbrite banner (9.6MB)
    ("1VHrM0wEQDWZZ2CMfPuHDy0_0UgcxVFyu", "metamersion-eventbrite.png"),
    # Metamersion banner (8MB)
    ("1JhOeSf6q9Pw_zsusXTLOQGjT0vKA3YuQ", "metamersion-banner-large.png"),
    # Metamersion banner alt (3.3MB)
    ("1R1PsCrlXgTNkz16WLWhMPL7khbkd6zkA", "metamersion-banner-alt.png"),
    # Metamersion social/Instagram posts (installation imagery)
    ("10SOogq5i5FWU3bMbBpn_lSI1gZd8olgC", "metamersion-installation-01.png"),
    ("1JemoPBHjFBEBE3EDIk5XLD4Wgo6nzGIR", "metamersion-installation-02.png"),
    ("1dWQqJFJIu27M6owwHmI_7C2F5AoGETk-", "metamersion-installation-03.png"),
    # Metamersion "opens tomorrow" series
    ("1aqLpNI-mmJX6aACQZk-pjBOkfVI4csWy", "metamersion-opens-tomorrow-1.png"),
    ("1UTm40lrQIVOX69kf1OqUGEASCzfqKaax", "metamersion-opens-tomorrow-2.png"),
    ("1dhQsJB92XCAQXwdl0aYXqgDVz_Rfxgea", "metamersion-opens-tomorrow-3.png"),
    # Latent Spaces 17 Dec versions (launch promo)
    ("18junsuR5ykdSBPy-qJkLKMFHgnL6xtgl", "metamersion-latentspaces-promo-1.png"),
    ("1xKQ4ttdxubr33SmZxAePI0IbhUaG-6e0", "metamersion-latentspaces-promo-2.png"),
    # Latent Spaces logo
    ("1nTHUrcUrXSO24fs5LwfEer7xWWLlSIyz", "latent-spaces-logo.png"),
]


def refresh_token():
    with open(CREDS_PATH) as f:
        creds = json.load(f)["installed"]
    with open(TOKENS_PATH) as f:
        tokens = json.load(f)
    resp = requests.post("https://oauth2.googleapis.com/token", data={
        "client_id": creds["client_id"],
        "client_secret": creds["client_secret"],
        "refresh_token": tokens["refresh_token"],
        "grant_type": "refresh_token",
    })
    resp.raise_for_status()
    return resp.json()["access_token"]


def download_file(file_id, filename, token):
    path = os.path.join(OUT_DIR, filename)
    url = f"https://www.googleapis.com/drive/v3/files/{file_id}?alt=media"
    resp = requests.get(url, headers={"Authorization": f"Bearer {token}"}, stream=True)
    if resp.status_code != 200:
        print(f"  FAILED {filename}: HTTP {resp.status_code} — {resp.text[:200]}")
        return None
    with open(path, "wb") as f:
        for chunk in resp.iter_content(8192):
            f.write(chunk)
    size = os.path.getsize(path)
    print(f"  OK {filename} ({size:,} bytes)")
    return size


def main():
    print("Refreshing access token...")
    token = refresh_token()
    print(f"Token refreshed. Downloading {len(TARGETS)} files...\n")

    total = 0
    ok = 0
    for file_id, filename in TARGETS:
        size = download_file(file_id, filename, token)
        if size:
            total += size
            ok += 1

    print(f"\nDone: {ok}/{len(TARGETS)} files, {total:,} bytes total ({total/1024/1024:.1f} MB)")


if __name__ == "__main__":
    main()
