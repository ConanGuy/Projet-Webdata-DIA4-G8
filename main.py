def main():
    from Trip import Trip
    
    dicTrip = Trip.load()
    print(len(dicTrip))
    
if __name__ == "__main__":
    main()