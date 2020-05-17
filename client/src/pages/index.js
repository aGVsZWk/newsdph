import Loadable from "react-loadable";
import Loading from "@/components/Loading";


// 路由懒加载，解决首屏慢
const Article = Loadable({
  loader: () => import ("./Article"),
  loading: Loading,
});
const Dashboard = Loadable({
  loader: () => import ("./Dashboard"),
  loading: Loading,
});
const Login = Loadable({
  loader: () => import ("./Login"),
  loading: Loading,
});
const NotFound = Loadable({
  loader: () => import ("./NotFound"),
  loading: Loading,
});
const Setting = Loadable({
  loader: () => import ("./Setting"),
  loading: Loading,
});
const Notify = Loadable({
  loader: () => import ("./Notify"),
  loading: Loading,
});

const FileExport = Loadable({
  loader: () => import("./FileExport"),
  loading: Loading,
});

const ReduxTest = Loadable({
  loader: () => import("./ReduxTest"),
  loading: Loading,
});

export {
  Article,
  Dashboard,
  Login,
  NotFound,
  Setting,
  Notify,
  FileExport,
  ReduxTest
};
