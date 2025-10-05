import cv2
import random
from ultralytics import YOLO

model = YOLO('yolov8n.pt') 

riddles = {
    # Original Riddles
    "I have a screen but no face. I bring the world to your living space. What am I?": "tv",
    "I have keys but open no doors. I have space but no room. You can enter but can't go outside. What am I?": "keyboard",
    "I have a neck but no head, and I wear a cap. What am I?": "bottle",
    "I have ribs but no spine. I'm your best friend when it rains. What am I?": "umbrella",
    "I'm a fruit that's long and yellow. Monkeys think I'm a fine fellow. What am I?": "banana",

    # New Riddles based on YOLO objects
    "I have a face but no eyes, and hands but no arms. What am I?": "clock",
    "I have a spine but no bones. I'm filled with stories for you to see. What am I?": "book",
    "I have legs but cannot walk. You use me when you want to sit. What am I?": "chair",
    "I have a screen and keys, but I'm small enough to take anywhere. What am I?": "laptop",
    "I have a tail, but I'm not an animal. I help you click and scroll. What am I?": "mouse",
    "I can run, but I have no legs. I have a bed, but I never sleep. What am I?": "river", # From 'boat' context
    "I have an eye but cannot see. You use me to thread your way through. What am I?": "needle", # From 'scissors' context
    "I have many buttons but no clothes. I let you change the channel from your couch. What am I?": "remote",
    "I bark but I'm not a tree. I'm known as man's best friend. What am I?": "dog",
    "I have a handle but I'm not a door. You use me for a hot drink. What am I?": "cup",
    "I have a head full of bristles. You use me every morning and night to keep your smile bright. What am I?": "toothbrush",
    "I have four wheels and doors, and I take you places on the road. What am I?": "car",
    "I have straps but no shoes. I'm carried on your back and hold your books. What am I?": "backpack",
    "I have three eyes: red, yellow, and green. I tell cars when to stop and go. What am I?": "traffic light",
    "I keep your food cold and have a door, but you can't live inside me. What am I?": "refrigerator",
    "I have blades that open and close, but I'm not a mouth. I'm used for cutting paper. What am I?": "scissors",
    "I have legs but I don't walk. You rest on me at the end of the day. What am I?": "bed",
    "I have a screen and can make calls, and I fit right in your pocket. What am I?": "cell phone"
}

riddle_list = list(riddles.items())

game_state = "ASK_RIDDLE"
current_riddle = ""
correct_answer = ""

print("--- Welcome to RiddleCam! ---")
print("I will ask you a riddle. Guess the object, then show it to the camera!")
print("Type 'quit' at any time to exit.")

while True:
    if game_state == "ASK_RIDDLE":
        current_riddle, correct_answer = random.choice(riddle_list)
        print("\n" + "="*30)
        print("Here is your riddle:")
        print(f"> {current_riddle}")
        game_state = "WAITING_FOR_GUESS"

    elif game_state == "WAITING_FOR_GUESS":
        user_guess = input("What is your guess? > ").lower().strip()
        
        if user_guess == 'quit':
            break

        if user_guess == correct_answer:
            print(f"\nCORRECT! The answer is '{correct_answer}'.")
            print("Now, prove it! Show the object to the camera.")
            game_state = "DETECTING_OBJECT"
        else:
            print("Not quite! Try again.")
            
    elif game_state == "DETECTING_OBJECT":
        cap = cv2.VideoCapture(0)
        object_found = False
        
        print("Searching for the object... Press 'q' to close the camera.")

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.flip(frame, 1)
            
            results = model(frame, conf=0.6, verbose=False)
            
            for result in results:
                for box in result.boxes:
                    cls = int(box.cls[0])
                    class_name = model.names[cls] 
                    
                    if class_name == correct_answer:
                        print(f"I see a {class_name}! Well done!")
                        object_found = True
                        break
                if object_found:
                    break
            
            annotated_frame = results[0].plot()
            cv2.imshow("RiddleCam - Show me the object!", annotated_frame)

            if object_found:
                cv2.waitKey(2000)
                break
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        
        if not object_found:
            print("Camera closed. Let's try another riddle.")
        
        game_state = "ASK_RIDDLE"

print("\nThanks for playing RiddleCam!")