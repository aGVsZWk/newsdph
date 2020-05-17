import {Article, Dashboard, Login, NotFound, Setting, Notify, FileExport, ReduxTest} from "@/pages";

const commonRoutes = [
  {
    pathname: "/login",
    component: Login,
  }, {
    pathname: "/404",
    component: NotFound,
  },
  {
    pathname: "/redux",
    component: ReduxTest,
  },
];

const privateRoutes = [
  {
    pathname: "/admin/dashboard",
    component: Dashboard,
    title: "仪表盘",
    isTop: true,
  }, {
    pathname: "/admin/article",
    component: Article,
    title: "文章管理",
    isTop: true,
  }, {
    pathname: "/admin/setting",
    component: Setting,
    title: "系统设置",
    isTop: true,
  }, {
    pathname: "/admin/notify",
    component: Notify,
    title: "通知中心",
    isTop: false,
  }, {
    pathname: "/admin/file-export",
    component: FileExport,
    title: "文件导出",
    isTop: false,
  },
];


export {
  commonRoutes,
  privateRoutes,
};
