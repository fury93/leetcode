var ImmutableHelper = function(obj) {
    this.original = obj;
    this.mutated = false;

    this.getPartialClone = (ori, cur) => {
        // Collect the keys encountered by ori during get calls and set them in
        // cur. And set the value bound for ori in cur.
        const setTrap = (target, prop, value) => {
            if (target[prop] !== value) {
                cur[prop] = value;
                this.mutated = true;
            }
{
