using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BackgroundRotator : MonoBehaviour
{
    [SerializeField] float RotationRate = 10f;
    float RotationMul = 1f, SpeedUp = 500f, TimeTillSpeedUp = 0;

    void Update()
    {
        transform.Rotate(0f, 0f, RotationRate * RotationMul * Time.deltaTime);
        TimeTillSpeedUp++;
        if(TimeTillSpeedUp > SpeedUp){ //speed up rotation every 500 frames
            TimeTillSpeedUp = 0;
            RotationMul += 0.2f;
        }

        if(RotationMul > 2){ //if rotation is doubled rotate in the other direction and start decreasing
            RotationMul = -RotationMul;
        }
    }
}
