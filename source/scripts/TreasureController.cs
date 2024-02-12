using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TreasureController : MonoBehaviour
{ 
    private float timePassed;
    // Start is called before the first frame update
    void Start()
    {
        timePassed = 0f;
    }

    // Update is called once per frame
    void Update()
    {
        timePassed += Time.deltaTime;
        if (timePassed > 1f)
        {
            transform.position = new Vector3(Random.Range(-5f, 5f), Random.Range(-5f, 5f), 0.0f);
            timePassed = 0f;
        }
    }
    void OnTriggerExit2D(Collider2D other)
    {
        p.score += 1;
    }
}

