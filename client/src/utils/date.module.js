const getDate = () => {
  const date = new Date();
  const year = date.getFullYear(); // 年
  let month = date.getMonth() + 1; // 月
  let day = date.getDate(); // 日
  if (month >= 1 && month <= 9) {
    month = `0${month}`;
  }
  if (day >= 0 && day <= 9) {
    day = `0${day}`;
  }
  return `${year}-${month}-${day}`;
};

const getPrevDate = () => {
  const myDate = new Date();
  const lw = new Date(myDate - (1000 * 60 * 60 * 24 * 30));
  const lastY = lw.getFullYear();
  const lastM = lw.getMonth() + 1;
  const lastD = lw.getDate();
  return `${lastY}-${lastM < 10 ? `0${lastM}` : lastM}-${lastD < 10 ? `0${lastD}` : lastD}`;
};

export default {
  getDate,
  getPrevDate,
};
