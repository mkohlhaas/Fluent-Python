#/bin/bash
for i in {1..20}; do echo -n "$i ";./procs.py $i | tail -1; done
