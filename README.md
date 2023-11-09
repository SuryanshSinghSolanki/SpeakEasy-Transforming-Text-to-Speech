# SpeakEasy-Transforming-Text-to-Speech
This web application is a Text-to-Speech (TTS) tool that allows users to convert text into speech using machine learning models. It utilizes Torchaudio and Streamlit to create a user-friendly interface for generating and playing audio from text.

Table of Contents <br>
*Getting Started <br>
*Prerequisites <br>
*Installation <br>
*Usage <br>
*Running the Application <br>
*File Structure <br>
*Customization <br>
*Contributing <br>
*License <br>
*Getting Started <br>
*Prerequisites <br>
Before you can run this application, ensure you have the following prerequisites installed: <br>
<br>
Python 3.x <br> 
Required Python packages (streamlit, torchaudio, soundfile) <br>
CUDA-compatible GPU (for efficient TTS model usage) <br>
Installation <br>
Clone this repository to your local machine: <br>
<br>
bash <br>
Copy code <br>
git clone [https://github.com/your-username/text-to-speech-app.git](https://github.com/SuryanshSinghSolanki/SpeakEasy-Transforming-Text-to-Speech.git) <br>
Navigate to the project directory: <br>
 <br>
bash <br>
Copy code <br>
cd text-to-speech-app <br>
Install the required Python packages: <br>
<br>
bash <br>
Copy code <br>
pip install -r requirements.txt <br>
Usage <br>
Running the Application <br>
To run the Text-to-Speech application, follow these steps: <br>
<br>
Open a terminal and navigate to the project directory. <br>
<br>
Run the Streamlit app with the following command: <br>
<br>
bash <br>
Copy code <br>
streamlit run main.py <br>
The application should open in your web browser. You can enter text in the input field and click the "Generate and Play Audio" button to convert the text to speech. <br>
<br>
File Structure <br>
main.py: The main Streamlit application script.<br>
utils.py: Contains utility classes and functions for TTS and audio manipulation.<br>
requirements.txt: Lists the required Python packages for the application.<br>
Customization<br>
You can customize this application in the following ways:<br>
<br>
Modify the user interface (e.g., styling, layout) in main.py.<br>
Adjust TTS model parameters in TTSUtils in utils.py to fit your specific use case.<br>
Integrate additional TTS models or improve the existing one.<br>
Enhance error handling and user feedback.<br>
Contributing<br>
Contributions are welcome! If you have ideas, improvements, or bug fixes, please submit a pull request. Make sure to follow the contribution guidelines.<br>

For any queries mail me: suryanshsolanki10@gmail.com
