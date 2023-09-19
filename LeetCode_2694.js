class EventEmitter {
  /*
  52 ms, faster than 70.42%
  */
  map = {}

  subscribe(event, cb) {
    if (!(event in map)) {
      this.map[event] = [];
    }
    this.map[event].push(cb);

    return {
        unsubscribe: () => {
          this.map[event] = this.map[event].filter(func => func !== cb);
        }
    };
  }

  emit(event, args = []) {
    if (!(event in this.map)) {
      return [];
    }
    return this.map[event].map(func => func(...args));
  }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */