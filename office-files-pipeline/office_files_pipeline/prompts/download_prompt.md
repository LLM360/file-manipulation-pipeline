You are downloading a single file from the public web.

- URL: {raw_url}
- Original path (use the basename as the saved filename): {file_path}

Save the downloaded file with its original filename (the basename of the
path above) inside the current working directory. The filename should not
include any subdirectory components — keep it as a single top-level file.

Tools you may install (outside the working directory; use mktemp -d / -t
and uv-managed venvs in /tmp):

- curl, wget, python+requests, python+httpx, etc.

After the download, verify the file exists and is non-empty.

## Terminal markers (you MUST write exactly one)

- **Success:** `echo <absolute_path_to_file> > .done` (single-line absolute
  path of the downloaded file). The file itself stays in the working
  directory next to the marker.

- **Skip / failure:** `touch .no_file` (empty marker). Use this when:
  - The file is larger than {max_size_mb}MB and downloading is wasteful.
  - The URL returns 404, requires authentication you don't have, or
    cannot be retrieved for any reason after reasonable retry.
  - You cannot fetch the file for any other reason but the work is
    complete (you tried).

  When writing `.no_file`, do NOT also write `.done`, and do NOT leave a
  partial file in the working directory.

## What must NOT happen

- Do not write both `.done` and `.no_file`.
- Do not write `.done` without leaving the downloaded file in the working
  directory — the worker validator will detect this and force a retry.
- Do not save the file under a subdirectory; everything must be at the
  top level of the working directory.
- Do not pollute the working directory with downloaded helper tools or
  scratch files; install those under /tmp.

Additional metadata about the source (raw URL, repo, file extension,
SHA, etc.) is also available in `task.json` if you need it for context.
