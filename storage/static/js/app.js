import Alpine from "alpinejs";
import * as Turbo from "@hotwired/turbo";

window.Alpine = Alpine;

Alpine.store("sidebar", {
  open: false,

  toggle() {
    this.open = !this.open;
  },
});

Alpine.store("searchbox", {
  open: false,

  toggle() {
    this.open = !this.open;
  },
});

Alpine.start();

Turbo.start();
