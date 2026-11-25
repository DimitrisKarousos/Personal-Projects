using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Cube : MonoBehaviour
{
    float movAmount = 1.5f, startPos;

    void Start(){
        startPos = transform.position.z;
    }

    void Update()
    {
        // move back and forth along the z axis
        transform.position += new Vector3(0f, 0f, movAmount * Time.deltaTime);
        if(transform.position.z > 2 * startPos){
            movAmount = -movAmount;
        }
        if(transform.position.z < startPos){
            movAmount = -movAmount;
        }
    }
}
