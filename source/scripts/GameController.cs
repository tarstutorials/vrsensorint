using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class GameController : MonoBehaviour
{
    public int score;
    static private int finalTime;
    public TextMeshProUGUI timeText;
    public TextMeshProUGUI scoreText;
    static public bool running;
    void Start()
    {
        score = 0;
        finalTime = 0;
    }

    // Update is called once per frame
    void Update()
    {
        if (score < 10){
            timeText.text = ("Time: " + (int)Time.time);
            scoreText.text = ("Score: " + score);
        }
        else{
            if (finalTime == 0){
                finalTime = (int)Time.time;
            }
            timeText.text = ("");
            scoreText.text = ("Congratulations! You got 10 score in " + finalTime + " seconds!");
        }

    }
}
