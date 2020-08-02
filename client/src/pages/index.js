import Loadable from "react-loadable";
import Loading from "@/components/Loading";


// 路由懒加载，解决首屏慢
export const Article = Loadable({
  loader: () => import ("./Article"),
  loading: Loading,
});
export const Dashboard = Loadable({
  loader: () => import ("./Dashboard"),
  loading: Loading,
});
export const Login = Loadable({
  loader: () => import ("./Login"),
  loading: Loading,
});
export const NotFound = Loadable({
  loader: () => import ("./NotFound"),
  loading: Loading,
});
export const Setting = Loadable({
  loader: () => import ("./Setting"),
  loading: Loading,
});
export const Notify = Loadable({
  loader: () => import ("./Notify"),
  loading: Loading,
});

export const FileExport = Loadable({
  loader: () => import("./FileExport"),
  loading: Loading,
});

export const FileUpload = Loadable({
  loader: () => import("./FileUpload"),
  loading: Loading,
});

export const VideoPlay = Loadable({
  loader: () => import("./VideoPlay"),
  loading: Loading,
});


export const BlackMusic = Loadable({
  loader: () => import("./BlackMusic"),
  loading: Loading,
});


export const TodoList = Loadable({
  loader: () => import("./TodoList"),
  loading: Loading,
});
