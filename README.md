## Observed weakness in V1: what failed and why
I believe when looking at V1 the weaknesses are that the rules relied on non-rotated and descaled layouts that didnt match up with each other which is why when I ran the test i got back about 31 rejections. 

## Design decision for V2: what Rule 4 is and why you chose it
Rule 4 is feature based image matching and I chose it because I noticed the faliure points in v1 and for it to no longer fail I needed the system to still be able to identify an image even if it was rotated or the scaling changed.

## Effect of the change: accuracy before/after on easy vs hard
When trying to determine accuracy I compared my results of the V1 hard test vs the V2 test. In the v1 test without any change to the rules there were 31 rejections but when V2 was used with a modification to Rule 4, 135 images were processed with a 53 match rate and a 82 rejection rate. 

## Trade-offs: what new costs or risks did Rule 4 introduce
Rule 4 makes the computer work harder so you can group that into a cost/risk of running an advanced rule checking process like that. There is also the risk of false positives happening because of similar images.
