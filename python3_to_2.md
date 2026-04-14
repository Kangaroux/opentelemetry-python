Migrate this library to be python2.7 compatible. An agent has already started the work on this.

There are two virtualenvs available:
- `.venv27` for python2.7
- `.venv37` for python3.7

There is also a refactoring script that an agent wrote: `./refactor_to_py27.py`. This script may need to be updated, it has been overly aggressive at times. The script does NOT need to cover every case. It should, however, be stable and reliable on the cases it *does* cover. The remaining work can be done manually.

Other important guidelines:
- Commit changes frequently
- Divide and conquer the work using subagents. The scope of this refactor is far too large for a single agent to do
- Validate the refactor often by compiling files or running tests
- Type hints do not need to be kept
- Use the two-dot syntax for git: `main..HEAD`. do NOT use the three-dot syntax, the branch is based off an older commit of `main`

# Agent-to-agent Notes
This section is for you (the agent) to use. Leave brief notes for future agents. Include things that worked well, didn't work well, a brief progress report, and anything else worth mentioning.
