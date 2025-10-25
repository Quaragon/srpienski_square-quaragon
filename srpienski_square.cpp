#include "turtle.hpp"
// turtle v C++
void srpienski_square(Turtle& t, float size, int n) {
    if (n < 0) {
        return;
    } else if (n == 0) {
        t.begin_fill();
        for (int i = 0; i < 4; ++i) {
            t.forward(size);
            t.left(90);
        }
        t.end_fill();
    } else {
        srpienski_square(t, size/3, n-1);
        for (int i = 0; i < 3; ++i) {
            t.forward(size/3);
            srpienski_square(t, size/3, n-1);
            t.forward(size/3);
            srpienski_square(t, size/3, n-1);
            t.forward(size/3);
            t.left(90);
        }
        t.forward(size/3);
        srpienski_square(t, size/3, n-1);
        t.forward(size/1.5);
        t.left(90);
    }
}

int main() {
    screen_size(1000, 800);
    Turtle t;
    t.set_speed(0);
    t.penup();
    t.go_to(-200, -150);
    t.pendown();
    t.right(90);

    srpienski_square(t, 400, 2);

    mainloop();
}