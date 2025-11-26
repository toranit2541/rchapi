USE [Ruamchai]
GO

/****** Object:  Table [dbo].[token_blacklist_outstandingtoken]    Script Date: 11/26/2024 2:42:27 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[token_blacklist_outstandingtoken](
	[id] [bigint] IDENTITY(1,1) NOT NULL,
	[token] [nvarchar](max) NOT NULL,
	[created_at] [datetimeoffset](7) NULL,
	[expires_at] [datetimeoffset](7) NOT NULL,
	[user_id] [int] NULL,
	[jti] [nvarchar](255) NOT NULL,
 CONSTRAINT [token_blacklist_outstandingtoken_id_69982597_pk] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY],
 CONSTRAINT [token_blacklist_outstandingtoken_jti_hex_d9bdf6f7_uniq] UNIQUE NONCLUSTERED 
(
	[jti] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

ALTER TABLE [dbo].[token_blacklist_outstandingtoken]  WITH CHECK ADD  CONSTRAINT [token_blacklist_outstandingtoken_user_id_83bc629a_fk_auth_user_id] FOREIGN KEY([user_id])
REFERENCES [dbo].[auth_user] ([id])
GO

ALTER TABLE [dbo].[token_blacklist_outstandingtoken] CHECK CONSTRAINT [token_blacklist_outstandingtoken_user_id_83bc629a_fk_auth_user_id]
GO


