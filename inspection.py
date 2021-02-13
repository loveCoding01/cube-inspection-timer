from time import perf_counter
import pyttsx3 as speaker
import threading
import sys

# Speak function for text-to-speech
def speak(audio):
    engine = speaker.init()
    engine.say(audio)
    engine.runAndWait()

# Wait function to detect when person has finished inspection
def wait():
    # Make stop_threads variable to False
    global stop_threads
    stop_threads = False
    # Get the start time of inspection
    start_time = perf_counter()
    # Wait for the person to click enter to finish inspection
    input()
    end_time = perf_counter()
    time = round(end_time - start_time, 2)
    # Print inspection time
    print('Inspection took', time, 'seconds')
    print(status)
    # Set stop_threads to True
    stop_threads = True

def inspection():
    # Set global variable status
    global status
    status = 'Valid'
    # Set start time
    start_time = perf_counter()
    # 8 seconds
    while perf_counter() - start_time < 8:
        if stop_threads:
            return

    speak('8 seconds')
    # 12 seconds
    while round(perf_counter() - start_time) < 12:
        if stop_threads:
            return
    speak('12 seconds')
    # +2
    while round(perf_counter() - start_time) < 15:
        if stop_threads:
            return    
    status = '+2'
    speak('Plus 2')
    # DNF
    while round(perf_counter() - start_time) < 18:
        if stop_threads:
            return
    status = 'DNF'
    speak('DNF')

def main():
    while True:
        # Ask user if they when they are starting inspection
        ask_for_inspection = input('Are you ready for inspection (y/n): ')
        if ask_for_inspection.lower() != '' and ask_for_inspection.lower() != 'y':
            # Exit system if they don't enter 'y' or ''
            sys.exit()
        # Make 2 threads
        wait_thread = threading.Thread(target = wait)
        inspection_thread = threading.Thread(target = inspection)
        # Start both
        wait_thread.start()
        inspection_thread.start()
        # Wait for both of them to finish
        wait_thread.join()
        inspection_thread.join()
# Start main function
if __name__ == '__main__':
    main()