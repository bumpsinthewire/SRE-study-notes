data "local_file" "global_policy" {
  filename = "global_policy.txt"
}

resource "local_file" "project_folder" {
  filename = "${var.project_name}/README.txt"
  content  = "Project: ${var.project_name}\nEnvironment: ${var.environment}\n${data.local_file.global_policy.content}"
}

resource "local_file" "log_file" {
  filename   = "${var.project_name}/activity.log"
  content    = "Log initialized for ${var.project_name}"
  depends_on = [local_file.project_folder]
}
