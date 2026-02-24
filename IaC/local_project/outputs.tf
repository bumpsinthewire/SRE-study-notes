output "readme_location" {
  value       = local_file.project_folder.filename
  description = "The path to the generated project README"
}
