using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TitleCard : MonoBehaviour
{
    public GameObject canvas; 
    //public GameObject strtBtn;
    //public GameObject qtBtn;


    // Start is called before the first frame update
    void Start()
    {
        canvas.SetActive(true);
        // start panel & buttons are active


        // initialize everything - directories of items & yokai
        List<object> curseDir = Repository.ReadItems("Curses");


    }

    // Update is called once p er frame
    void Update()
    {
        // when start button is pressed start the game

        // when end button is pressed end (?) -- how to quit 
    }
}
