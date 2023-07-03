"""Rename the downloaded youtube videos to official video names."""
from pathlib import Path
import subprocess
from tqdm import tqdm
import glob
import os.path as osp


dir_name = "RD"
video_dir = f"/d/dataset/audio/HDTF_DATA/{dir_name}25_images"
video_files = glob.glob(osp.join(video_dir, "*"))
video_names = [Path(v).with_suffix("").name for v in video_files]

with open(f"HDTF_dataset/{dir_name}_video_url.txt", 'r') as f:
    urls = [l.strip().split() for l in f.readlines()]

print(f"Local files:{len(video_files)}\nOfficial files:{len(urls)}")
for name, url in urls:
    local_name = url.split("?")[-1][2:]
    print(name, local_name, local_name in video_names)
    if not (local_name in video_names):
        continue
    idx = video_names.index(local_name)
    # print(idx)
    p = Path(video_files[idx])
    # print(p.suffix)
    new_name = Path(video_dir) / f"{name}{p.suffix}"
    Path(video_files[idx]).rename(new_name)
    # print(new_name)

# NOTE: Clip videos
# dir_name = "WDA"
# video_dir = f"/d/dataset/audio/HDTF_DATA/{dir_name}25"
# save_dir = f"/d/dataset/audio/HDTF_DATA/{dir_name}25_clip"
# with open(f"HDTF_dataset/{dir_name}_annotion_time.txt", 'r') as f:
#     snipptes = [l.strip().split() for l in f.readlines()]
# for file, *snippte in snipptes:
#     video_file = osp.join(video_dir, file)
#     if not osp.exists(video_file):
#         continue
#     # print(video_file, snippte)
#     p = Path(file)
#     suffix = p.suffix
#     name = p.with_suffix("").name
#     for i, s in enumerate(snippte):
#         start, end = s.split('-')
#         # print(start, end)
#         subprocess.run(
#             [
#                 "ffmpeg",
#                 "-i",
#                 f"{video_file}",
#                 "-ss",
#                 f"{start}",
#                 "-to",
#                 f"{end}",
#                 f"{save_dir}/{str(name)}_{i}{suffix}",
#             ]
#         )

# NOTE: udpate the name of images.
# im_dirs = glob.glob("/d/dataset/audio/HDTF_DATA/RD25_images/*")
# for im_dir in tqdm(im_dirs, total=len(im_dirs)):
#     im_files = sorted(glob.glob(osp.join(im_dir, "*")), key=lambda x: int(Path(x).with_suffix("").name), reverse=True)
#     for im_file in im_files:
#         p = Path(im_file)
#         suffix = p.suffix
#         name = int(p.with_suffix("").name)
#         new_name = p.parent / f"{name + 1}{suffix}"
#         p.rename(new_name)
