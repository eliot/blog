Title: How to use Microsoft FTP on cmd.exe
Date: 2019-07-05 
Category: Tech

This is a brief tutorial on how to use Microsoft's FTP client (ftp.exe) provided on Windows using the command line (cmd.exe).

Start FTP in interactive mode.

    > ftp

Connect to a server:

    ftp> open myserver.com

    Connected to myserver.com.
    220 My FTP Server
    200 UTF8 set to on

Or you can connect with the initial `ftp` command:

    > ftp myserver.com

Enter your login credentials:

    User (myserver.com:(none)): joe
    331 Password required for joe
    Password:
    230 User joe logged in
