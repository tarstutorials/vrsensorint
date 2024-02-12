using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
            if (Input.GetKey("w")){
                transform.Translate(0.0f,0.02f, 0.0f);
            }
            if (Input.GetKey("a")){
                transform.Translate(-0.02f, 0.0f,0.0f);
            }
            if (Input.GetKey("s")){
                transform.Translate(0.0f, -0.02f, 0.0f);
            }
            if (Input.GetKey("d")){
                transform.Translate(0.02f, 0.0f, 0.0f);
            }
    }
}
