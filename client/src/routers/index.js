// import {Article, Dashboard, Login, NotFound, Setting, Notify, FileExport,
//         VideoPlay, FileUpload} from "@/pages";
//
// const commonRoutes = [
//   {
//     pathname: "/login",
//     component: Login,
//   },
//   {
//     pathname: "/404",
//     component: NotFound,
//   }
// ];
//
// const privateRoutes = [
//   {
//     pathname: "/admin/dashboard",
//     component: Dashboard,
//     title: "仪表盘",
//     isTop: true,
//   },
//   {
//     pathname: "/admin/article",
//     component: Article,
//     title: "文章管理",
//     isTop: true,
//   },
//   {
//     pathname: "/admin/setting",
//     component: Setting,
//     title: "系统设置",
//     isTop: true,
//   },
//   {
//     pathname: "/admin/notify",
//     component: Notify,
//     title: "通知中心",
//     isTop: false,
//   },
//   {
//     pathname: "/admin/file-export",
//     component: FileExport,
//     title: "文件导出",
//     isTop: false,
//   },
//   {
//     pathname: "/admin/file-upload",
//     component: FileUpload,
//     title: "文件上传",
//     isTop: true,
//   },
//   {
//     pathname: "/admin/video-play",
//     component: VideoPlay,
//     title: "视频播放",
//     isTop: true,
//   },
// ];


// export const CommonRouteSwitch = (
//   {
//     commonRoutes.map((item, index) => {
//       return (<Route key={item.pathname} path={item.pathname} component={item.component}></Route>)
//     })
//   }
// )
//
// export const PrivateRouteSwitch = () => {
//   return ({
//     privateRoutes.map((item, index) => {
//       return (
//         <Route
//           key={item.pathname}
//           path={item.pathname}
//           render={(rootProps) => {
//             return <item.component {...rootProps} />;
//           }} />
//         )
//       })
//     })
//   }
