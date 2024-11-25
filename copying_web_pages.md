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

