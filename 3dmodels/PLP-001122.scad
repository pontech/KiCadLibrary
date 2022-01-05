echo(version=version());
in2mm = 25.4;
mm2in = 1/in2mm;

body_w = 3.20;
body_l = 0.44;
body_h = 1.00;

stud_w = (2.9 - 1) / 2;
stud_l = (body_w - 2.7) / 2;
stud_h = .1;
stud_x = stud_w / 2 + 0.2;
stud_y = (body_w - stud_l) / 2;


bcut_w = 3.60;
bcut_h = 2.20;

lens_d = 2.00;
lens_h = 1.00;
lens_x = 0.00;
lens_y = 0.24;


$fn = 50;

color("white")
{
    // Body
    linear_extrude(height = body_h) square([body_w, body_l], true);
   
}
color("blue")
{
    difference() {
        translate([lens_x, lens_y, 0.05]) 
            linear_extrude(height = lens_h-0.1) circle(d=lens_d);

        translate([lens_x, -body_l, -0.1]) 
        linear_extrude(height = lens_h+0.2) square([body_w, body_l*2], true);
    }
}


// Written in 2015 by Torsten Paul <Torsten.Paul@gmx.de>
