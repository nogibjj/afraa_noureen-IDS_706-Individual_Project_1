"""test_main module"""
import main

def test_main():
    '''
    testing function for system
    '''
    assert len(main.display_system_info()) != 0

if __name__ == "__main__":
    test_main()
    
