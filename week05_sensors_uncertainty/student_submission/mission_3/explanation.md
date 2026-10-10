# Mission 3

## Assistive.prediction_draft

Now by increasing weight and changing to moving avg we can get even more error than before, and potentially a dangerous command. Like the last test, this scenario would be challenged by the baseline.

## Warehouse.prediction_draft

Last run, will try one more time to reduce delay and unnecessary stop, and by using the same settings as the first run but with a moving average threshold, it might help reduce the dangerous commands.

## context_comparison

in the second to last policy of the warehouse robot, we got 2 dangerous commands and high delay which may have caused injury to any operators or may have damaged to equipment. The final policy of warehouse robot's results closely resembles the baseline, despite the fact that it is in a moving average configuration with a slightly lower sensor weight than the baseline. 

## error_costs

Different people bear false safe and unnecessary stop costs. In all results of the warehouse simulation, we can see that unnecessary stopping was constantly on 0.0408, but this didn't necessarily lead to any dangerous commands, so at worst we have the company potentially losing money for slow warehouse flow. But when we made changes to configuration and window size, then we started getting dangerous commands, so there could be some damage to inventory/equipment.

## limitations

The seven tests establish how each sensor reacts in different scenarios, and they also allow us to infer what could go wrong at certain times during these scenarios. However they do not establish the desired outcomes and for that we need to consult the client/user, and for testing we need to choose which one resembles the user's desired outcome, or create a new motion test all together.
