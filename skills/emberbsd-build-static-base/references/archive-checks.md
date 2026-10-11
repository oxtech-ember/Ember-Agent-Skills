# Archive and deployment checks

Set `base_set`, `listing`, and `candidate` to the actual outputs.

```sh
tar -tf "$base_set" > "$listing"
rg '(\.so([./]|$)|ld\.elf_so)' "$listing"
file "$candidate/bin/sh"
```

Require a successful archive listing and a statically linked shell.
For the search, status 1 means no shared libraries or loader were found.
Status 2 means the search failed.
Archive extraction does not remove obsolete `.so` files.

For authorized deployment, follow the OS recovery and installation procedure.
Keep coherent artifacts, chroot checks, target MAKEDEV definitions, and a rollback archive.
Record hashes for the board radio firmware overlay.
After restarting critical services, verify a new SSH login before reboot.
Then check the running kernel revision, memfd, floating-point contracts, and network.
Record set hashes, commands, results, and gaps.

Historical Pi5 acceptance on 2026-10-10/11 used OS revision `383e2a9dc502eeddab2abb6a628580737cbba0b3`.
Static rc completion took about eight seconds; dynamic rc completion took about six seconds.
The archives measured 144MiB and 36MiB respectively.
Static linking removes loader and library synchronization requirements.
Those measurements do not establish faster boot.
Recorded static sshd, public-key login, dhcpcd, and WPA3/SAE results qualify only that tested Pi5 configuration.
