# Copying Web Pages
This is a tutorial on how to create a static version of any webpage to serve as the front end for a CTF.

This method is used in the creation of the CWRU Student Information System (SIS) CTF.

After following this method and copying web pages, modifications can be made, and backends can be connected to allow for exploits.

---

## Download WebScrapBook

To copy the HTML and assets from a dynamic website, use the Firefox (install [here](https://www.mozilla.org/en-US/firefox/new/)) plugin WebScrapBook (install [here](https://addons.mozilla.org/en-US/firefox/addon/webscrapbook/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search)).

![image](https://github.com/user-attachments/assets/a5f9eb95-15fd-45fe-993d-c8d08e2349cc)

---

## Take a Capture of the Webpage

Navigate to whatever webpage you want to copy; for this example, I will copy the SIS class list tab.

Next, open the WebScrapBook plugin (click the puzzle piece in the top left to open the plugin menu).

When opened, select `Capture Tabs`  (do __not__ capture tabs as a bookmark or source), and a file should be downloaded to your computer.

![image](https://github.com/user-attachments/assets/ed5240a3-764c-402a-a365-f182579238a9)

---

## Open the Code

In your downloads folder, there should be a directory called `WebScrapBook/`. Navigate to `WebScrapBook/data/.../` where `...` is a generated string containing the date. __NOTE__: If you create multiple captures, they will be saved in this directory with different `...` fields for date/time.

 ![image](https://github.com/user-attachments/assets/8125987b-d74a-4495-bf37-1b4e151986fb)

To ensure all went well, find the file `index.html` and open it in the browser. It should look very similar to the source material but with all of the dynamic elements disabled. 

In this example, the class search page looks identical. However, the search bar and all of the buttons do nothing. (Notice that the URL bar on Chrome shows that this file is local on my system, not on the SIS server).

![image](https://github.com/user-attachments/assets/a9365257-6295-4251-ba72-f4f691751045)

---

## Cleaning Up the Code

This is possibly the most tedious and annoying part of this whole process, as there is not much visual difference, and it takes time. Still, we need it for maintainability and sanity.

Start by copying the folder with the date/time string into another directory and renaming it to something more useful. In this example, I renamed the folder `class_search_page/` and put it on my desktop.

![image](https://github.com/user-attachments/assets/875e61f1-6d99-411d-ac54-5eb8be2aa954)

Now open this copied folder in your favorite IDE, for this example I will be using VSCode.

![image](https://github.com/user-attachments/assets/9c223a03-4fa7-4ba1-a025-167786eb8ebb)

Now, here comes the tedious part: Currently, all of the webpage assets (CSS files, images, fonts, etc.) are all jumbled together in the folder, which makes it hard to work with. To fix this, we will be creating an `assets/` folder with subdirectories for the different kinds of assets. Here is what the end product should look like:

![image](https://github.com/user-attachments/assets/f955949d-c0e4-4063-815c-6e21171cdc0b)

After moving all of the files to their new directories and trying to open the HTML file, you will likely see that it is broken. __This is expected__:

![image](https://github.com/user-attachments/assets/0ac1c262-94c0-47f8-8106-65413e3da2a8)

This is because the paths __within__ the files themselves are still pointing to the main directory, even though the files are already there. This means that none of the files can reference each other.
