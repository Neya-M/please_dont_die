# please_dont_die

<img alt="full render" src="https://cdn.hackclub.com/019ed8ef-6f04-7f04-98ff-19593a782153/render.png" />

please_dont_die is an automated greenhouse that can detect water moisture and temperature and regulate them with fans and an automated irrigation system.

I made this because I would often forget to water my plants and my garden ended up having a half life of a few days. Almost all of my plants are dead and the rest are there by luck. I didn't want this to happen again next year, so my solution? Unpaid Raspberry pi labor! I probably don't need a whole Raspberry pi for this but it's what I have :P

## Why does it look so lame

The vision was to create a big greenhouse with lots of types of sensors and a lot of area to grow plants, but I didn't have enough time to finish designing it and I don't have enough money to make that too. So I made a super extra really tiny version of it that can only save one plant from my terrible watering skills. After I get the small version working, I hope to get a grant from Hack Club to finish the large version. Speaking of Hack Club, you should definitely join if you are between 13-18 and like to make stuff! hackclub.com

## How does it work?

So far, I have a small gardening pot for the plant to grow in and half of a plastic bottle to trap moisture inside. There's also a fan (which is just a propeller attatched to a simple hobby motor) and an irrigation system (which is a tray of water leading into a valve that can be opened and closed to drip water into the pot). Controlling those are a Raspberry Pi Pico with a thermometer and a humidity sensor.

## How do I make it?

I'm flattered that you would actually want to build this (at least at this stage)! But if you really do, you can grab the parts in my BOM and wire it up like so:

<img alt="Wiring diagram" src="https://cdn.hackclub.com/019ed8ef-6c5b-7af2-a9ad-b7c4a5942db4/image.png" />

Print out the files in my CAD folder, there are both STL and STEP files. Make sure to print out the silicone lid in silicone! It might work in regular plastic but it will fit and stop water a lot better when flexible.

Then get a plant pot, put your lucky plant in it, and cut off the bottom of a plastic container. Put the plastic over your pot and cut holes in it to hold your water tray. Attach the plastic tube to the water tray and then the solenoid valve, securing the valve there with the bracket.
 Add a propeller to the motor and wire it to the pi pico, and solder the heat sensor onto the pi pico via some wires. Route the valve wires into the raspberry pi box and attach those too. You should also probably add some sealant in the holes so that water doesn't go in accidentally.

## Other stuff

This was made for Hack Club's Fallout program.

Onshape link: https://cad.onshape.com/documents/1dc20001da3f647674e4c842/w/ed51346f8b0a2bd125ba8456/e/2d2d3c608c60d9f7610b3506

Zines:

<img alt="Zine" src="https://cdn.hackclub.com/019ed8f9-24ed-7128-b8aa-b9eec9c74931/zine.png" />

<img alt="Left page" src="https://cdn.hackclub.com/019ed8f9-278a-7084-bc0d-35ff2f253bf9/left_page.png" />

<img alt="Right page" src="https://cdn.hackclub.com/019ed8f9-2a8c-7d63-a149-8ffcf352e5a8/right_page.png" />
