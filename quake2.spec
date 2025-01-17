%define icculus_version r0.16.1
%define rogue_source	roguesrc320
%define xatrix_source	xatrixsrc320
%define	Summary		Quake II

Summary:	%{Summary}
Name:		quake2
Version:	3.21_r0.16.1
Release:	12
URL:		https://icculus.org/projects/quake2/
Source0:	%{name}-%{icculus_version}.tar.bz2
Source1:	%{rogue_source}.tar.bz2
Source2:	%{xatrix_source}.tar.bz2
Source6:	q2ded.sh
Source7:	q2ded.cfg
Source8:	q2ctf.sh
Source9:	q2ctf.cfg
Source11:	%{name}_16.png
Source12:	%{name}_32.png
Source13:	%{name}_48.png
Group:		Games/Arcade
License:	GPL
Patch0:		quake2-chris.patch
Patch1:		quake2-fix_build.patch
Patch2:		quake2-allow_softx_on_x86_64.patch
Patch3:		quake2-build_softsdl_on_x86_64.patch
# fix undefined mremap (create errors on x86_64)
Patch4:		quake2-fix_mremap.patch
Patch5:		quake2-r0.16.1-fix-alsa-sound-driver.patch
BuildRequires:  SDL-devel
BuildRequires:	aalib-devel
BuildRequires:	libx11-devel
BuildRequires:	libxext-devel
BuildRequires:	libxxf86dga-devel
BuildRequires:	libxxf86vm-devel
BuildRequires:	svgalib-devel

%description
Shortly after landing on an alien surface you learn that hundreds of your men
have been reduced to just a few.  Now you must fight your way through heavily
fortified military installations, lower the city's defenses and shut down
the enemy's war machine.  Only then will the fate of humanity be known.

* Larger, mission-based levels:

You have a series of complex missions, what you do in one level could affect
another.  One false move and you could alert security, flood an entire
passageway, or worse.

* Superior artificial intelligence:

This time the enemy has IQs the size of their appetites.  The can evade your
attack, strategically position themselves for an ambush and hunt your ass 
down.

* In-your-face sound and graphics

hear distant combat explosions and rockets whizzing past your head.  And with
a compatible 3-D graphics accelerator, experience smoother 16-bit graphics and
real-time lighting effects.

* Wicked multiplayer capabilities

More than 32 players, friends or foes, can do at it in a bloody deathmatch via
LAN and over the internet.

-- You need PAK files for Quake II to run this game --

Install the PAK files in %{_gamesdatadir}/quake2.


%package	svga
Summary:	Quake II SVGA client
Group:		Games/Arcade
Requires:	%{name} = %{version}

%description	svga
This archive contains Quake II for SVGALib Console Graphics.

-- You need PAK files for Quake II to run this game --

%package	x11
Summary:	Quake II X11 client
Group:		Games/Arcade
Requires:	%{name} = %{version}

%description	x11
This archive contains Quake II for X11.

-- You need PAK files for Quake II to run this game --

%package	glx
Summary:	Quake II GLX client
Group:		Games/Arcade
Requires:	%{name} = %{version}

%description	glx
This archive contains Quake II for GLX.

-- You need PAK files for Quake II to run this game --

%package	sdl
Summary:	Quake II SDL client
Group:		Games/Arcade
Requires:	%{name} = %{version}

%description	sdl
This archive contains Quake II for SDL.

-- You need PAK files for Quake II to run this game --

%package	aa
Summary:	Quake II aalib client
Group:		Games/Arcade
Requires:	%{name} = %{version}

%description	aa
This archive contains Quake II for aalib.

-- You need PAK files for Quake II to run this game --

%package	ctf
Summary:	Quake II Capture the Flag for Linux
Group:		Games/Arcade
Requires:	%{name} = %{version} %{name}-server = %{version}
Requires(preunt):	rpm-helper
Requires(post):	rpm-helper

%description	ctf
Quake II Capture The Flag (Q2CTF) is a multiplayer addon for Quake2 that 
features a simple set of rules for team based play. It features eight unique 
maps and special powerups to enhance and make the gameplay more exciting.

Q2CTF requires the full retail version of Quake II installed in order to 
play. Once installed, you simple need to connect to a Quake2 game server 
that is running the Q2CTF addon.

-- You need PAK files for Quake II to run this game --

#
#
###
%package	xatrix
Summary:	Quake II Mission Pack #1: "The Reckoning" for Linux
Group:		Games/Arcade
Requires:	%{name} = %{version}

%description	xatrix
This archive contains Mission Pack "The Reckoning" for Quake II.

The Reckoning is sure to get your heart pumping...well, if you can avoid 
getting gibbed by the Strogg. Check out just some of the features below that 
will give you the cardiac workout you need!

* 18 arduous levels to conquer & 7 brutal deathmatch exclusive levels:

Dive into a series of mission-based campaigns and ransack your way through 
three all-new hazardous episodes. Experience bioluminescent life forms, 
stalagmites and stalactites and other breathtaking environments. 

* Fresh foes to defeat:

Gekks are lighting-fast creatures that will hunt you down, leaping from the 
shadows to claw or bite. Though innocent looking, the Repair Bot has the 
ability to awaken dead Strogg from eternal sleep.
 
* Added weapons to wield:

The Phalanx Particle Canon emits a pulsing stream of deadly energy into 
unsuspecting foes. 

The Trap sucks nearby enemies inside and turns them into food cubes for 
player consumption. 

The Ion Ripper fires a blast of glowing boomerangs capable of ricocheting 
off of walls to track targets.

-- You need PAK files for Quake II to run this game --

#
#
###
%package	rogue
Summary:	Quake II Mission Pack #2: "Ground Zero" for Linux
Group:		Games/Arcade
Requires:	%{name} = %{version}

%description	rogue
This archive contains Mission Pack "Ground Zero" for Quake II.

The Alien Assault Continues.
Take out the Big Gun, sounded simple enough, except the Stroggs were waiting. 
You and a few Marines like you, are the lucky ones. The Gravity Well, the 
Stroggs' newest weapon in its arsenal against mankind, is operational. You've 
made it down in one piece and are still able to contact the fleet. With the 
fleet trapped around Stroggos, five percent of ground forces surviving, and 
that number dwindling by the second, your orders have changed: Free your 
comrades in orbit. Destroy the Gravity Well!

New Enemies

Get ready to face the toughest horde of Stroggs, straight from the bio-vats. 
The Stalker, Turrets, Daedalus, Medic Commander, Carrier and the Queen Bitch 
herself, the Black Widow.
     
14 Entirely new levels and 10 new deathmatch levels

Brand new real estate with the same dynamic sense of reality and dramatic 
visuals as Quake II. These new environments will challenge even the biggest 
Quake II aficionado.
 
New Power-ups

Tag 'em and Bag 'em. Deathmatch specific power-ups: the Vengeance Sphere, 
Hunter Sphere, and Anti-matter Bomb. With everything that we've cooked up for 
you here, you're sure to annihilate anyone or anything foolish enough to 
call you foe.

New Weapons 

The Chainsaw, ETF Rifle, and Plasma Beam. If you can't get the job done with 
these babies, it's time to go back to Basic.

Accept no substitutes!
Official, id-authorized mission packs outpace the rest!

-- You need PAK files for Quake II to run this game --

#
#
###
%package	server
Summary:	Quake II server
Group:		Games/Arcade
Requires:	%{name}
Requires(preun):	rpm-helper
Requires(post):	rpm-helper

%description server
This archive contains the Quake II dedicated server.

-- You need PAK files for Quake II to run this game --


%prep
%setup -q -T -b 0 -n %{name}-%{icculus_version}
%setup -q -T -D -a 1 -n %{name}-%{icculus_version}
%setup -q -T -D -a 2 -n %{name}-%{icculus_version}
%patch0 -p1 -b .chris
%patch1 -p1 -b .fix_build
%patch2 -p0 -b .allow_softx_on_x86_64
%patch3 -p0 -b .build_softsdl_on_x86_64
%patch4 -p1
%patch5 -p1 -b .alsa~

# Patch Makefile
sed -e "s|-malign|-falign|g" -i Makefile

# Patch rogue source
sed -e "s|<nan\.h>|<bits/nan.h>|" -i %{rogue_source}/g_local.h

%build
%define _disable_ld_no_undefined 1
%ifarch %{ix86} x86_64
export OPTFLAGS="-O2 -ffast-math -funroll-loops -falign-loops=2 -falign-jumps=2 -falign-functions=2 -fno-strict-aliasing"
%else
export OPTFLAGS="%{optflags} -ffast-math -funroll-loops -fomit-frame-pointer -fexpensive-optimizations"
%endif

%make	build_release \
	BUILD_SDLQUAKE2=YES \
	BUILD_SVGA=YES \
	BUILD_X11=YES \
	BUILD_GLX=YES \
	BUILD_FXGL=NO \
	BUILD_SDL=YES \
	BUILD_SDLGL=YES \
	BUILD_CTFDLL=YES \
	BUILD_XATRIX=YES \
	BUILD_ROGUE=YES \
	BUILD_JOYSTICK=YES \
	BUILD_ARTS=NO \
	BUILD_DEDICATED=YES \
	BUILD_AA=YES \
	BUILD_QMAX=NO \
	STATICSDL=NO \
	SDLDIR=%{_libdir} \
	XATRIX_DIR=%{xatrix_source} \
	ROGUE_DIR=%{rogue_source} \
	CC="gcc $OPTFLAGS %{ldflags}"

%install
# Install dirs
install -d %{buildroot}%{_sysconfdir}/quake2/{baseq2,ctf,rogue,xatrix}
install -d %{buildroot}%{_gamesbindir}
install -d %{buildroot}%{_gamesdatadir}/quake2/{baseq2,ctf,rogue,xatrix}
install -d %{buildroot}%{_libdir}/games/quake2/{baseq2,ctf,rogue,xatrix}

# Install files
cp release%{_arch}/ref_*.so %{buildroot}%{_libdir}/games/quake2/
cp release%{_arch}/quake2 %{buildroot}%{_gamesbindir}/quake2.bin
cp release%{_arch}/q2ded %{buildroot}%{_gamesbindir}/q2ded.bin
cp release%{_arch}/sdlquake2 %{buildroot}%{_gamesbindir}/sdlquake2.bin
cp release%{_arch}/game%{_arch}.so %{buildroot}%{_libdir}/games/quake2/baseq2/
cp release%{_arch}/ctf/game%{_arch}.so %{buildroot}%{_libdir}/games/quake2/ctf/
cp release%{_arch}/rogue/game%{_arch}.so %{buildroot}%{_libdir}/games/quake2/rogue/
cp release%{_arch}/xatrix/game%{_arch}.so %{buildroot}%{_libdir}/games/quake2/xatrix/

install -m644 %{SOURCE7} -D %{buildroot}%{_sysconfdir}/quake2/baseq2/server.cfg
install -m644 %{SOURCE9} -D %{buildroot}%{_sysconfdir}/quake2/ctf/server.cfg

install -m755 %{SOURCE6} -D %{buildroot}%{_initrddir}/q2ded
install -m755 %{SOURCE8} -D %{buildroot}%{_initrddir}/q2ctf

for FILE in q2ded q2ctf ; do

    # Edit path to q2ded in initscript
    sed -i -e "s|daemon[ ].*\${NAME}|daemon %{_gamesbindir}/\${NAME}|" %{buildroot}%{_initrddir}/${FILE}

    # Edit path to %{_sysconfdir} in initscript
    sed -i -e "s|^Q2_CONFIGDIR=.*|Q2_CONFIGDIR=\"%{_sysconfdir}/quake2\"|" %{buildroot}%{_initrddir}/${FILE}
done

# Create wrapper scripts
cat << EOF > %{buildroot}%{_gamesbindir}/quake2
#!/bin/sh

%{_gamesbindir}/quake2.bin +set basedir %{_libdir}/games/quake2 \$*

exit 0
EOF

cat << EOF > %{buildroot}%{_gamesbindir}/sdlquake2
#!/bin/sh

%{_gamesbindir}/sdlquake2.bin +set basedir %{_libdir}/games/quake2 \$*

exit 0
EOF

cat << EOF > %{buildroot}%{_gamesbindir}/q2ded
#!/bin/sh

%{_gamesbindir}/q2ded.bin +set basedir %{_libdir}/games/quake2 \$*

exit 0
EOF

# Icons
install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

# Menu
%{__mkdir_p} %{buildroot}%{_datadir}/applications

cat << EOF > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Name=Quake II
Comment=%{Summary}
Exec=%{_gamesbindir}/quake2
Icon=%{name}
Terminal=true
Type=Application
StartupNotify=false
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF


cat << EOF > %{buildroot}%{_datadir}/applications/mandriva-%{name}-xatrix.desktop
[Desktop Entry]
Name=Quake II: The Reckoning
Comment=%{Summary}
Exec=%{_gamesbindir}/quake2 +set game xatrix
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF


cat << EOF > %{buildroot}%{_datadir}/applications/mandriva-%{name}-rogue.desktop
[Desktop Entry]
Name=Quake II: Ground Zero
Comment=%{Summary}
Exec=%{_gamesbindir}/quake2 +set game rogue
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF


cat << EOF > %{buildroot}%{_datadir}/applications/mandriva-%{name}-ctf.desktop
[Desktop Entry]
Name=Quake II: Capture The Flag
Comment=%{Summary}
Exec=%{_gamesbindir}/quake2 +set game ctf
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

# Create links from basedir to configdir
ln -sf %{_sysconfdir}/quake2/baseq2/server.cfg %{buildroot}%{_libdir}/games/quake2/baseq2/server.cfg
for FILE in pak0.pak pak1.pak pak2.pak maxpak.pak ; do
    ln -sf %{_gamesdatadir}/quake2/baseq2/${FILE} %{buildroot}%{_libdir}/games/quake2/baseq2/${FILE}
done
ln -sfn %{_gamesdatadir}/quake2/baseq2/video %{buildroot}%{_libdir}/games/quake2/baseq2/video
ln -sf %{_sysconfdir}/quake2/ctf/server.cfg %{buildroot}%{_libdir}/games/quake2/ctf/server.cfg
ln -sf %{_gamesdatadir}/quake2/ctf/pak0.pak %{buildroot}%{_libdir}/games/quake2/ctf/pak0.pak
ln -sf %{_gamesdatadir}/quake2/rogue/pak0.pak %{buildroot}%{_libdir}/games/quake2/rogue/pak0.pak
ln -sf %{_gamesdatadir}/quake2/xatrix/pak0.pak %{buildroot}%{_libdir}/games/quake2/xatrix/pak0.pak

%post server
%_post_service q2ded

%preun server
%_preun_service q2ded

%_post_service q2ctf

%preun ctf
%_preun_service q2ctf

%files
%doc README TODO src/docs/3.21_Changes.txt
%attr(755,root,root) %{_gamesbindir}/quake2
%{_gamesbindir}/quake2.bin
%dir %{_libdir}/games/quake2
%{_libdir}/games/quake2/baseq2
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_gamesdatadir}/quake2/baseq2

%ifnarch x86_64
%files svga
%{_libdir}/games/quake2/ref_soft.so
%endif

%files x11
%{_libdir}/games/quake2/ref_softx.so

%files glx
%{_libdir}/games/quake2/ref_glx.so

%files sdl
%attr(755,root,root) %{_gamesbindir}/sdlquake2
%{_gamesbindir}/sdlquake2.bin
%{_libdir}/games/quake2/ref_sdlgl.so
%{_libdir}/games/quake2/ref_softsdl.so

%files aa
%{_libdir}/games/quake2/ref_sdlgl.so
%{_libdir}/games/quake2/ref_softaa.so

%files server
%attr(755,root,root) %{_initrddir}/q2ded
%attr(755,root,root) %{_gamesbindir}/q2ded
%dir %{_sysconfdir}/quake2
%dir %{_sysconfdir}/quake2/baseq2
%config(noreplace) %{_sysconfdir}/quake2/baseq2/server.cfg
%{_gamesbindir}/q2ded.bin

%files ctf
%doc src/ctf/docs/*.gif src/ctf/docs/*.html src/ctf/docs/*.jpg
%attr(755,root,root) %{_initrddir}/q2ctf
%dir %{_sysconfdir}/quake2/ctf
%config(noreplace) %{_sysconfdir}/quake2/ctf/server.cfg
%{_libdir}/games/quake2/ctf
%{_gamesdatadir}/quake2/ctf
%{_datadir}/applications/mandriva-%{name}-ctf.desktop

%files rogue
%{_libdir}/games/quake2/rogue
%{_gamesdatadir}/quake2/rogue
%{_datadir}/applications/mandriva-%{name}-rogue.desktop

%files xatrix
%{_libdir}/games/quake2/xatrix
%{_gamesdatadir}/quake2/xatrix
%{_datadir}/applications/mandriva-%{name}-xatrix.desktop
