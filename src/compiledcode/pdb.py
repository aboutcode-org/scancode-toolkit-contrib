"""
Notes:

http://permalink.gmane.org/gmane.comp.gnu.mingw.user/34002
http://www.codeproject.com/Articles/37456/How-To-Inspect-the-Content-of-a-Program-Database-P
https://github.com/moyix/pdbparse
http://forensicswiki.org/wiki/Executable#MZ.2C_PE.2FCOFF
http://moyix.blogspot.be/2008/05/parsing-windows-minidumps.html
https://support.microsoft.com/en-us/kb/121366
http://www.debuginfo.com/articles/debuginfomatch.html

http://sourceforge.net/p/mingw-w64/code/HEAD/tree/experimental/tools/libmsdebug/
https://code.google.com/p/google-breakpad/wiki/SymbolFiles
https://github.com/netsarang/crashfix/blob/8c1f9f220b968e41cf8de00d15d30c1ed1f230e6/crashfix_service/libdumper/License.cpp
https://github.com/zhmz90/valgrind/blob/9078cd93596ffa2a13d7abab5398ba93d378f53e/coregrind/m_debuginfo/readpdb.c#L353
https://github.com/zhmz90/valgrind/blob/9078cd93596ffa2a13d7abab5398ba93d378f53e/coregrind/m_debuginfo/debuginfo.c
https://github.com/CSRedRat/RosWine/blob/935418cb3c2732c1fb9733d24bfa18f6d79cec15/dlls/dbghelp/msc.c#L2531

https://github.com/wine-mirror/wine
https://github.com/wine-mirror/wine/tree/master/tools/winedump
https://source.winehq.org/WineAPI/dbghelp.html
http://wiki.winehq.org/WineOnWindows
http://wiki.winehq.org/mingw-w64?action=show&redirect=CompilingDLLsUsingMingw
http://www.kegel.com/wine/wow.html

http://lld.llvm.org/windows_support.html

https://bitbucket.org/pombredanne/breakpad
https://code.google.com/p/google-breakpad/wiki/LinuxStarterGuide#Producing_symbols_for_your_application
https://code.google.com/p/google-breakpad/wiki/GettingStartedWithBreakpad
https://chromium.googlesource.com/breakpad/breakpad/+/master/docs/symbol_files.md
And also a python parsing tool

https://stuff.mit.edu/afs/sipb/project/wine/src/wine-0.9.37/tools/winedump/README
http://wine-wiki.org/index.php/WineLib

https://github.com/wine-mirror/wine/tree/master/tools/winedump


https://github.com/dezelin/kBuild
https://github.com/dezelin/kBuild/blob/1046ac4032f3b455d251067f46083435ce18d9ad/src/kmk/kmkbuiltin/kDepIDB.c#L119


winedump dump filters: "(/src/files/|Source file:|file=)"



wine IRC chat
[15:09] <pombreda> Howdy :) I am looking to hack winedump .... the goal would be to build it as a shared object and build a python binding for it...
[15:09] <pombreda> puk:  do you think building winedump as a shared lib is feasible?
[15:10] <@aeikum> hetii: right. so you can search a +relay log for that message, and then work backwards to see what failed and caused that message to be displayed
[15:11] <nsivov> pombreda, is it not enough to just call it from python?
[15:11] <pombreda> nsivov: the output would need to be parsed ... unless there is a trick in dump to get a structured output?
[15:12] <puk> pombreda: you could add an XML output mode
[15:12] * puk whistles
[15:12] <puk> right nsivov ?
[15:12] <puk> ;)
[15:12] <hetii> 15MB of log :/
[15:12] <nsivov> puk, sure, it's a native program, i don't care
[15:13] <pombreda> puk: some structured output would be nice (on the dump side)... may be json rather xml  :P
[15:14] <hetii> 0009:Call user32.MessageBoxA(0001008c,00cb1364 "Invalid user name or password. Try again.",00cb139c "...",00000010) ret=00431313
[15:14] <puk> sure
[15:14] <pombreda> puk: nsivov: would you knwo if the printing well structured in one place /a few function or scattered all around?
[15:14] <pombreda> *is well structured
[15:16] <puk> it's been a while since I worked on it
[15:16] <pombreda> puk: I found you name in the manpage ;) hence why I bug you
[15:17] <puk> and I was wondering how you tracked me down
[15:17] <puk> as I don
[15:17] <pombreda> puk: the answer is that printing seems scattered :|
[15:17] <@aeikum> hetii: 15 MB is a very small relay log :) i often deal with gigabytes
[15:17] <puk> as I don't feature prominently in git log
[15:18] <puk> look at that
[15:18] <puk> I indeed worked on the man page
[15:18] <pombreda> puk: :) You were the one that had a nick I found from the names ;)
[15:19] <pombreda> and one of thew few recent (3 yeasr ago) committer to debug.c
[15:19] <puk> but that predates even CVS it seems
[15:19] <puk> pombreda: Andre_H has recently done work on it
[15:20] * julliard adds puk in the maintainers file
[15:20] <puk> julliard: nice try!
[15:20] <pombreda> :D
[15:21] <puk> julliard: I'm astonished that you didn't add me to DirectMusic yet
[15:21] <pombreda> julliard: would you know if winedump builds on Windows and Mac beyond Linux?
[15:21] <pombreda> (builds and run
[15:21] <@aeikum> i'll send a patch to add /dev/null as the dmusic maintainer
[15:22] <@julliard> pombreda: sure, it should
[15:22] <puk> pombreda: you should be able to cross compile it with mingw-w64 for Windows
[15:22] <nsivov> pombreda, winedump doesn't depend on anything, it's only about file io I think
[15:23] <puk> you just have to have that installed before running configure
[15:23] <puk> and then make crosscompile
[15:23] <pombreda> neato, that should be easy to try...  
[15:23] <nsivov> what are you trying to dump with it?
[15:24] <puk> limit yourself to tools/winedump/ for the crosscompile
[15:24] <pombreda> nsivov: a symbols dumper that can be used on windows/linux/mac for pe and pdbs... as a helper to trace a pe back to the sources used to compile it
[15:25] <pombreda> nsivov: I have the same type of code working nicely for elfs and dwarfs but that is mucho easier there ;)
[15:26] <pombreda> nsivov: so basically I need: the list of source files and the symbols from each, then this is matched back to a source tree
[15:27] <pombreda> puk:  about crosscompile, you mean I can compile winedump exes for Windows and Mac from Linux?
[15:27] <puk> for Windows
[15:27] <puk> no clue about Mac
[15:28] <pombreda> that is already a nice thing indeed
[15:28] <puk> but if you have a Mac you can compile it directly there
[15:28] <pombreda> Linux code usuallly compiles and runs mostly ok on mac, and I compile on mac for that
[15:29] <nsivov> did you search for existing python modules that do that?
[15:29] <nsivov> i see something called pdbparse on github
[15:29] <pombreda> nsivov: sure, there is a pdbparse that chokes on most and every basic pdb I throw at it, while winedump works very nicely
[15:29] <puk> hmm, that reminds me
[15:29] <nsivov> pombreda, ok
[15:29] <puk> julliard: is somebody using Wine Stable on MacOSX?
[15:30] <pombreda> nsivov: the alternative could be also google breakpad symbol dumper
[15:30] <pombreda> that seems to work on pdb and pes... I have not tested it yet
[15:30] <puk> slackner: your buildbot has a MacOSX box in it?
[15:30] <@julliard> puk: probably
[15:31] <pombreda> nsivov: though breakpad may not support older pe and pdb formats

 * PDB support
############# 
 https://channel9.msdn.com/Forums/Coffeehouse/Is-there-a-way-to-read-a-CC-PDB-file-contents
 http://reverseengineering.stackexchange.com/questions/2548/pdb-v2-0-file-format-documentation
 https://code.google.com/p/pdbparser/source/checkout
 https://code.google.com/p/pdbparse/
 http://www.codeproject.com/Articles/37456/How-To-Inspect-the-Content-of-a-Program-Database-P
 http://www.windbg.org/
 https://msdn.microsoft.com/en-us/windows/hardware/hh852365.aspx
 http://pykd.codeplex.com/
 https://github.com/pombredanne/GitIndex
 http://source.winehq.org/source/tools/winedump/pdb.c
 https://github.com/pombredanne/scripts-8\
 https://github.com/pombredanne/symstore
 http://source.roslyn.io/#Roslyn.Test.PdbUtilities/Pdb/Token2SourceLineExporter.cs


"""