; Script generated by the Inno Script Studio Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Subtitle Converter"
#define MyAppVersion "1.0.2"
#define MyAppPublisher "Nasime Shomal , Inc."
#define MyAppExeName "main.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{630813D6-8F4C-4706-8BB7-6DA43BD9EC46}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={pf}\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
OutputDir=C:\Users\Mahmood\PycharmProjects\SubtitleConverter\iss\Output
OutputBaseFilename=SubtitleConverter
SetupIconFile=C:\Users\Mahmood\PycharmProjects\SubtitleConverter\resources\srt.ico
Compression=lzma
SolidCompression=yes
VersionInfoVersion=1.0.2
VersionInfoProductName=Subtitle Converter
VersionInfoProductVersion=1.0.2

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 0,6.1

[Files]
Source: "C:\Users\Mahmood\PycharmProjects\SubtitleConverter\dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Mahmood\PycharmProjects\SubtitleConverter\dist\_bz2.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Mahmood\PycharmProjects\SubtitleConverter\dist\_ctypes.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Mahmood\PycharmProjects\SubtitleConverter\dist\_hashlib.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Mahmood\PycharmProjects\SubtitleConverter\dist\_lzma.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Mahmood\PycharmProjects\SubtitleConverter\dist\_socket.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Mahmood\PycharmProjects\SubtitleConverter\dist\_ssl.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Mahmood\PycharmProjects\SubtitleConverter\dist\_win32sysloader.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Mahmood\PycharmProjects\SubtitleConverter\dist\icudt53.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Mahmood\PycharmProjects\SubtitleConverter\dist\icuin53.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Mahmood\PycharmProjects\SubtitleConverter\dist\icuuc53.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Mahmood\PycharmProjects\SubtitleConverter\dist\library.zip"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Mahmood\PycharmProjects\SubtitleConverter\dist\pyexpat.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Mahmood\PycharmProjects\SubtitleConverter\dist\PyQt5.QtCore.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Mahmood\PycharmProjects\SubtitleConverter\dist\PyQt5.QtGui.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Mahmood\PycharmProjects\SubtitleConverter\dist\PyQt5.QtWidgets.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Mahmood\PycharmProjects\SubtitleConverter\dist\python34.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Mahmood\PycharmProjects\SubtitleConverter\dist\pywintypes34.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Mahmood\PycharmProjects\SubtitleConverter\dist\Qt5Core.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Mahmood\PycharmProjects\SubtitleConverter\dist\Qt5Gui.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Mahmood\PycharmProjects\SubtitleConverter\dist\Qt5Widgets.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Mahmood\PycharmProjects\SubtitleConverter\dist\select.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Mahmood\PycharmProjects\SubtitleConverter\dist\settings.ini"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Mahmood\PycharmProjects\SubtitleConverter\dist\sip.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Mahmood\PycharmProjects\SubtitleConverter\dist\unicodedata.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Mahmood\PycharmProjects\SubtitleConverter\dist\win32api.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\dist\platforms\*"; DestDir: "{app}\platforms"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files
Source: "..\dist\srt.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\dist\resources\*"; DestDir: "{app}\resources"; Flags: ignoreversion createallsubdirs recursesubdirs

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; WorkingDir: "{app}"; IconFilename: "{app}\srt.ico"; IconIndex: 0
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"; WorkingDir: "{app}"; IconFilename: "{app}\srt.ico"; IconIndex: 0
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; WorkingDir: "{app}"; IconFilename: "{app}\srt.ico"; IconIndex: 0; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: quicklaunchicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

[Dirs]
Name: "{app}\platforms"
Name: "{app}\resources"
