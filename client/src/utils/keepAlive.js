const keepAlive = (obj) => {
  obj.$api.public.keepAlive();
  // eslint-disable-next-line no-underscore-dangle
  if (obj._isDestroyed) {
    clearTimeout(obj.timerssss);
    // console.log(`摧毁了：${obj}`)
  } else {
    // console.log(`没有摧毁：${obj}`)
    // eslint-disable-next-line no-param-reassign
    obj.timerssss = setTimeout(() => {
      this.default(obj);
    }, 300000);
  }
};
export default keepAlive;
