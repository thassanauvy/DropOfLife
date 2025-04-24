export const fadeIn = {
    beforeEnter(el) {
      el.style.opacity = 0
    },
    enter(el, done) {
      el.style.transition = 'opacity 1s'
      el.style.opacity = 1
      done()
    }
  }
  