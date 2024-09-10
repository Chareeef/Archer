export interface DecodedToken {
  user_id: string;
  role: string;
  token_type: string;
  exp: number;
}

export interface Lesson {
  id: string;
  created_at: string;
  grade_level: number;
  subject: "English" | "Mathematics" | "Science";
  educator_id: string;
  educator_full_name: string;
  title: string;
  text: string;
  video_link: string | null;
}
