# Intelligent Avatars in Virtual Reality Environments
A project for developing intelligent avatars for use in virtual reality environments, using Unity and Ubiq.

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/MEBM1/intelligent_avatars_vr.git
````
### 2. Open the project in Unity
Download and open Unity Hub:
https://unity.com/

### 3. Open Unity and create a project
- Open **Unity Hub**
- Click on **"New Project"**
- Select the **3D (Core)** template
- Give your project a name (e.g., `IntelligentAvatarsVR`)
- Choose the location to save the project
- Click on **"Create"**


## Setup
### 1. Add package via Git URL

1. Open the **Package Manager**:
   - Go to `Window > Package Manager`

2. Click the **“+”** button in the top left corner

3. Select the option **“Add package from git URL…”**

4. In the text box that appears, paste the following URL: https://github.com/UCL-VR/ubiq.git#upm
5. Click **“Add”**

Unity will download and install the **Ubiq** package directly from GitHub.

### 2. Import the Demo to Test

1. In the **Package Manager**, click on the **Ubiq** package (on the left side).

2. On the right panel, go to **Samples**.

3. Click **Import** next to the **“Demo (XRI)”** option.

<img src="https://github.com/user-attachments/assets/6c4974ac-1891-4bcc-9aac-b685945095c8" width="700"/>


This will import the demo scene.

---

### 3. Open and Run the Demo Scene

1. In the **Project** panel (bottom panel), navigate to:
Assets > Samples > Ubiq > [version] > Demo (XRI)

3. Double-click on the **Demo.unity** file to open the scene.

4. Once the scene is loaded, click the **Play** button at the top of the screen to run the demo.
   
## Avatar Creation
### 1. Create Your Avatar

1. Go to: [https://readyplayer.me]([https://readyplayer.me](https://readyplayer.me/avatar?id=67fbf6c8e6ba077336eec969))

2. Click on **“Create Avatar”**.

3. Choose:
   - **Full body** or **head only** (I recommend **full body**).

4. Customize your avatar however you like.

5. Once finished, click **Next → Download for Unity (.glb)**.

6. In **Unity**, drag and drop the `.glb` file into the **Assets** folder in the **Project** panel. Wait for Unity to import the file.

7.  Drag the imported avatar model from the **Assets** folder to the **Hierarchy** panel to add it to your scene.

8. Adjust the position to `(0, 1, 0)` to ensure the avatar is not buried in the ground.

9. If the avatar appears too small, scale it up by setting the scale to something like `(10, 10, 10)` in the **Inspector** panel.

## Add Scripts to Unity

1. Add the scripts `LipSyncFromAudioClip.cs` and `AskMarie.cs` to your **Assets** folder in Unity.
   - You can either create them manually by right-clicking in the **Assets** panel → **Create > C# Script**, and pasting the code inside,
   - or drag the existing `.cs` files directly into the **Assets** folder from your file explorer.

2. After adding the scripts, Unity will compile them automatically. You should see no errors in the Console.
   
## Attach Scripts to a GameObject

1. In your scene, create an **Empty GameObject**:
   - Right-click in the **Hierarchy** panel → **Create Empty**
   - Rename it to `AvatarAssistant`

2. With `AvatarAssistant` selected:
   - In the **Inspector**, click on **Add Component**
   - Add Audio Source
   - Search for and add the scripts `LipSyncFromAudioClip` and `AskMarie`

### Fill in Script Fields in the Inspector

For the `LipSyncFromAudioClip` component, fill out the following fields:

- **Face Mesh** → Drag the `Wolf3D_Head` object (inside your avatar in the **Hierarchy**) into this field.  
  This object contains the blend shapes used for facial animation.

- **Mouth Blend Shape Index** → Keep it as `0`

- **Audio Source** → Drag the GameObject that contains your **Audio Source** component into this field.

For the `AskMarie` component, fill out the following fields:

- **Server Url** → write http://localhost:5000/speech-to-text-and-respond

- **Audio Source** → Drag the GameObject that contains your **Audio Source** component into this field.
<img src="https://github.com/user-attachments/assets/d9c801fe-0f5d-4fab-8f85-6b46fa53ffbe" width="400"/>

## Run the Code

1. Go to the `llm_server` directory and run the Python server script (preferable to create a anaconda env).

2. If everything is working correctly, open your Unity project.

3. Press the **`R`** key during play mode to start speaking with the avatar.

4. Wait for the avatar to respond based on the audio input and backend processing.
