# SiemensPLCPython
Repository to read inputs and write outputs on S7 1200 PLC using Python codes. Uses the snap7 library

#### The existing snap 7 library needs modifications to be able to properly execute the attached codes. Installation and modification steps are given below

1. Download gijzelaerr/python-snap7 version 2.0.2 and extract it
2. Navigate using terminal to the path of the extracted folder
3. Install using {pip install .}
4. Download snap7-full-1.4.2.7z from https://sourceforge.net/projects/snap7/files/1.4.2/. Alternatively you can use the attached files in the Snap 7 Installation folder.
5. Extract and copy release\Windows\Win64\snap7.dll
6. Paste snap7.dll to C:\Windows\System32
7. Next find out the path to the snap7 folder
![image](https://github.com/user-attachments/assets/c7b37094-5346-497c-8cdc-4efa6edfc23c)
8. Edit client.py file. Replace line 378 {if area not in Area:} with {if not isinstance(area, int):} and Replace line 388 {f"reading area: {area.name} db_number: {db_number} start: {start} amount: {size} "} with {f"reading area: {area} db_number: {db_number} start: {start} amount: {size} "}
9. Alternatively, you can replace the client.py file with the client.py file under the Replacement File folder within the Snap 7 Installation folder.

