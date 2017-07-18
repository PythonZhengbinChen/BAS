function jpage_main() {
	$("div.holder").jPages({
      containerID : "main_list",
      previous : "前一页",
      next : "后一页",
      perPage : 5,
      delay : 10
    });
}