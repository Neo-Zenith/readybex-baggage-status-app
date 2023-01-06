# ReadyBex

## How to Use
1. Visit [link](https://readybex.vercel.app) to access the baggage status. <br>
2. To access the check in kiosk, run **kiosk.ps1** in *scripts*.<br>
3. To access the scanner for Arduino Uno, run **scanner.ps1** in *scripts*. <br>

### Take note
* Remember to run ```pip install -r requirements.txt``` under the *arduino* sub-directory to install all dependencies required for the kiosk UI.
* Remember to load the sketch (found in *arduino/sketch*) into Arduino Uno board before Step 2 and 3. 
* Remember to change the COM port to match the COM port that you use to connect your Arduino board.

## Tech Used
<p>
  <img src="https://img.shields.io/badge/Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white" />
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" />
  <img src="https://img.shields.io/badge/Microsoft_Azure-0089D6?style=for-the-badge&logo=microsoft-azure&logoColor=white" />
</p>

## Interface
### Kiosk UI
#### Main Page
![image](https://user-images.githubusercontent.com/77436548/211071396-0b2cfac2-ecd5-4e5c-bf12-2bf1a4fe433a.png)

#### QR Code Display
![image](https://user-images.githubusercontent.com/77436548/211071541-70715c01-ec21-4a33-bbcc-2d490a09b180.png)

### Web App UI
![image](https://user-images.githubusercontent.com/77436548/211071731-ddff51b2-3a1c-421b-9c54-67e0c17a2c34.png)
