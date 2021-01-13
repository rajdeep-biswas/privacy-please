# Privacy please

Do you want to send files safely to your friends? This is the thing for you.  

### Setting up  
1. Download and install [ngrok](https://ngrok.com/download).
2. Make sure you have Python. (I used Python 3.7.0).  
3. Run `setup.bat` (and that's it).

### Creating encrypted files to be sent  
1. Put all your files within the `put_contents_here` folder.  
2. Run `zipup.bat`.  
3. Under `zipped` folder, the zip file that has been created is your encrypted file and the text file contains the password that your friend will need to be able to unlock it. Do not share the latter with anyone else (of course).  
4. Upload the file to the temporary website your friend is hosting - ask them for the URL of format `xyz.ngrok.io/` 
5. [Optional] Make sure you have sent everything that has to be sent and run `clean_folders.bat` to remove all of your contents from all folders.  

### Hosting the temporary server
1. Run start_server.bat (two terminals will open up) - the 'ngrok' one is of importance to us (the more colorful one).  
2. Give your friend the URL you find in above step.  
3. Once they upload the zip file, you will find you have received it under `uploads` folder.
4. Access it using the password they share with you.
