# please_dont_die

<img alt="full render" src="https://cdn.hackclub.com/019eddc8-23f6-753b-9e1c-b909791001d2/render.png" />

please_dont_die is an automated greenhouse that can detect water moisture and temperature and regulate them with fans and an automated irrigation system.

I made this because I would often forget to water my plants and my garden ended up having a half life of a few days. Almost all of my plants are dead and the rest are there by luck. I didn't want this to happen again next year, so I made this!

## Why does it look so lame

The vision was to create a big greenhouse with lots of types of sensors and a lot of area to grow plants, but I didn't have enough time to finish designing it and I don't have enough money to make that either. So I made a super extra really tiny version of it that can only save one plant from the hot, dry summers. After I get the small version working, I hope to get a grant from Hack Club to finish the large version. 

(about Hack Club, you should definitely join if you are between 13-18 and like to make stuff! https://hackclub.com/)

## How does it work?

So far, I have a small gardening pot for the plant to grow in and half of a plastic bottle to trap moisture inside. There's also a fan (which is just a propeller attatched to a simple hobby motor) and an irrigation system (which is a tray of water leading into a valve that can be opened and closed to drip water into the pot). Controlling those are a Raspberry Pi Pico with a thermometer and a humidity sensor. The battery is boosted up with a 
Powerboost 500 and it can signal the Raspberry Pi when the battery is low, so you can press the button to check and the pico will light up an LED if it needs replacing.

All you need to do is a bit of setup (see below) and a few battery changes!

## How do I make it?

I'm flattered that you would actually want to build this (at least at this stage)! But if you really do, you can grab the parts in my BOM and wire it up like so:

<img alt="Wiring diagram" src="https://cdn.hackclub.com/019edd2e-bf2b-7e23-8600-0f606cccd198/image.png" />

Print out the files in my CAD folder, there are both STL and STEP files. Make sure to print out the parts marked as silicone in silicone! They might work in regular plastic but they will fit and stop water a lot better when flexible.

Then get a plant pot, put your lucky plant in it, and cut off the bottom of a plastic container. (You can also use this in a different setup to drip water, if you want) Put the plastic over your pot and cut holes in it to hold your water tray. Attach the plastic tube to the water tray and then the solenoid valve, securing the valve there with the bracket.
Load the firmware onto the Raspberry Pi Pico.

 Add a propeller to the motor and wire it to the pi pico, and solder the DHT11 on it too. Route the valve wires into the raspberry pi box and attach those too. I recommend to glue the parts in place so they don't wiggle around and so that there aren't any little gaps for water to seep in.

## Other stuff

This was made for Hack Club's Fallout program.

Onshape link: https://cad.onshape.com/documents/1dc20001da3f647674e4c842/w/ed51346f8b0a2bd125ba8456/e/2d2d3c608c60d9f7610b3506

Zines:

<img alt="Zine" src="https://cdn.hackclub.com/019eddc8-57fe-733b-bd37-f2fb0635a343/zine.png" />

<img alt="Left page" src="https://cdn.hackclub.com/019eddc8-0311-7ac3-94bd-eda87d54e62e/Left%20page.png" />

<img alt="Right page" src="https://cdn.hackclub.com/019eddc8-3eed-720d-af07-5fc5605d0475/Right%20page.png" />
