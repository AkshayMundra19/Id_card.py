import os
from datetime import datetime, timedelta
import time
from playsound import playsound

# --- Configuration ---
SNOOZE_MINUTES = 5
TONES_DIRECTORY = "tones"

def get_alarm_details():
    """
    Gets the alarm time and desired tone from the user.
    """
    # 1. Get and validate alarm time
    while True:
        try:
            time_input = input("Enter alarm time in 24-hour format (HH:MM): ")
            alarm_time = datetime.strptime(time_input, "%H:%M").time()
            break
        except ValueError:
            print("Invalid format. Please use HH:MM.")

    # 2. Get and validate alarm tone
    if not os.path.exists(TONES_DIRECTORY) or not os.listdir(TONES_DIRECTORY):
        print("\n Warning: 'tones' directory is empty or not found.")
        print("The alarm will be silent. Please create the directory and add sound files.")
        return alarm_time, None

    tones = [f for f in os.listdir(TONES_DIRECTORY) if f.endswith(('.mp3', '.wav'))]
    
    if not tones:
        print("\n Warning: No .mp3 or .wav files found in the 'tones' directory.")
        return alarm_time, None

    print("\nAvailable Tones:")
    for i, tone in enumerate(tones):
        print(f"  {i + 1}. {tone}")

    while True:
        try:
            choice = int(input(f"Choose a tone (1-{len(tones)}): "))
            if 1 <= choice <= len(tones):
                selected_tone_path = os.path.join(TONES_DIRECTORY, tones[choice - 1])
                return alarm_time, selected_tone_path
            else:
                print(" Invalid choice. Please select a number from the list.")
        except ValueError:
            print(" Invalid input. Please enter a number.")


def trigger_alarm(tone_path):
    """
    Plays the alarm sound and handles snooze/stop logic.
    Returns True if snoozed, False if stopped.
    """
    print("\n Wake Up! It's time! ")
    while True:
        try:
            # Play the sound
            if tone_path:
                playsound(tone_path)
            else: # Fallback for no sound file
                print("RING! RING! RING!")
                time.sleep(5) # Wait 5 seconds for silent alarm
        except Exception as e:
            print(f"Error playing sound: {e}. Using text alert instead.")
            print("RING! RING! RING!")
            time.sleep(5)

        # Ask to snooze or stop
        user_choice = input("Press 's' to snooze or any other key to stop: ").lower()
        if user_choice == 's':
            print(f"Snoozing for {SNOOZE_MINUTES} minutes...")
            return True  # Indicates snoozed
        else:
            print("Alarm stopped.")
            return False # Indicates stopped


def main():
    """Main function to run the alarm clock."""
    print("--- Python Alarm Clock ---")
    
    alarm_time, tone_path = get_alarm_details()
    
    print(f"\n Alarm set for {alarm_time.strftime('%H:%M')}. Press Ctrl+C to exit.")
    
    try:
        while True:
            now = datetime.now().time()
            
            # Check if it's time for the alarm
            if now.hour == alarm_time.hour and now.minute == alarm_time.minute:
                should_snooze = trigger_alarm(tone_path)
                
                if should_snooze:
                    # Calculate new alarm time after snooze
                    snooze_time = datetime.now() + timedelta(minutes=SNOOZE_MINUTES)
                    alarm_time = snooze_time.time()
                    print(f"Next alarm at {alarm_time.strftime('%H:%M')}")
                else:
                    # User chose to stop, so exit the program
                    break
            
            # Wait for a second before checking again
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nProgram exited.")


if __name__ == "__main__":
    main()